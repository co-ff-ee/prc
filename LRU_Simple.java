

import java.io.*;

public class LRU_Simple {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        // --- input ---
        System.out.print("Enter number of frames: ");
        int frames = Integer.parseInt(br.readLine());
        System.out.print("Enter length of reference string: ");
        int ref_len = Integer.parseInt(br.readLine());

        int[] reference = new int[ref_len];
        System.out.println("Enter reference string (space or newline separated):");
        // Read the reference string numbers
        for (int i = 0; i < ref_len; i++) {
            reference[i] = Integer.parseInt(br.readLine());
        }

        // --- initialize frames and last-used times ---
        int[] buffer = new int[frames];   // stores page numbers currently in frames
        int[] lastUsed = new int[frames]; // stores "time" when each frame was last used
        for (int i = 0; i < frames; i++) {
            buffer[i] = -1;    // -1 means empty frame
            lastUsed[i] = 0;   // 0 means never used yet
        }

        int time = 0;   // logical clock (increases with each reference)
        int hits = 0, faults = 0;
        int[][] mem_layout = new int[frames][ref_len]; // for printing snapshots

        // --- core LRU loop ---
        for (int i = 0; i < ref_len; i++) {
            time++;                 // every reference increments time
            int page = reference[i];
            boolean isHit = false;

            // check if page already in any frame => hit
            for (int f = 0; f < frames; f++) {
                if (buffer[f] == page) {
                    hits++;
                    lastUsed[f] = time; // update last-used timestamp
                    isHit = true;
                    break;
                }
            }

            // if miss, place page in empty frame or replace LRU frame
            if (!isHit) {
                faults++;

                // try to find empty frame first
                int place = -1;
                for (int f = 0; f < frames; f++) {
                    if (buffer[f] == -1) {
                        place = f;
                        break;
                    }
                }

                // if no empty frame, find least recently used (smallest lastUsed)
                if (place == -1) {
                    int minIdx = 0;
                    for (int f = 1; f < frames; f++) {
                        if (lastUsed[f] < lastUsed[minIdx]) {
                            minIdx = f;
                        }
                    }
                    place = minIdx;
                }

                // put page into chosen frame and update lastUsed
                buffer[place] = page;
                lastUsed[place] = time;
            }

            // save snapshot for printing later
            for (int f = 0; f < frames; f++) {
                mem_layout[f][i] = buffer[f];
            }
        }

        // --- print results ---
        System.out.print("\nReference String: ");
        for (int v : reference) System.out.printf("%4d", v);

        System.out.println("\n\nMemory Layout (rows = frames):");
        for (int f = 0; f < frames; f++) {
            System.out.printf("F%-2d |", f + 1);
            for (int i = 0; i < ref_len; i++) {
                System.out.printf("%4d", mem_layout[f][i]);
            }
            System.out.println();
        }

        System.out.println("\n--------------------------------------");
        System.out.println("Total Hits   : " + hits);
        System.out.println("Total Faults : " + faults);
        System.out.printf("Hit Ratio    : %.2f\n", (float) hits / ref_len);
        System.out.println("--------------------------------------");
    }
}
