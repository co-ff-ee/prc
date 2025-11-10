package PAGE_REPLACEMENT;

import java.io.*;

public class FIFO {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int frames, pointer = 0, hit = 0, fault = 0, ref_len;
        int[] buffer;
        int[] reference;
        int[][] mem_layout;

        System.out.print("Enter the Number of Frames: ");
        frames = Integer.parseInt(br.readLine());

        System.out.print("Enter the Length of Reference String: ");
        ref_len = Integer.parseInt(br.readLine());

        reference = new int[ref_len];
        mem_layout = new int[frames][ref_len];
        buffer = new int[frames];

        for (int j = 0; j < frames; j++)
            buffer[j] = -1;

        System.out.println("Please enter the reference string:");
        for (int i = 0; i < ref_len; i++) {
            reference[i] = Integer.parseInt(br.readLine());
            int search = -1;

            for (int j = 0; j < frames; j++) {
                if (buffer[j] == reference[i]) {
                    search = j;
                    hit++;
                    break;
                }
            }

            if (search == -1) {
                buffer[pointer] = reference[i];
                fault++;
                pointer = (pointer + 1) % frames;
            }

            for (int j = 0; j < frames; j++) {
                mem_layout[j][i] = buffer[j];
            }
        }

        
        System.out.print("\nReference String: ");
        for (int i = 0; i < ref_len; i++) {
            System.out.printf("%3d ", reference[i]);
        }

        
        System.out.println("\n\nMemory Layout:");
        for (int i = 0; i < frames; i++) {
            System.out.printf("F%-2d |", i + 1);
            for (int j = 0; j < ref_len; j++) {
                if (mem_layout[i][j] == -1)
                    System.out.print("    "); 
                else
                    System.out.printf("%3d ", mem_layout[i][j]);
            }
            System.out.println();
        }

        
        System.out.println("\n--------------------------------------");
        System.out.println("Total Hits   : " + hit);
        System.out.println("Total Faults : " + fault);
        System.out.printf("Hit Ratio    : %.2f\n", (float) hit / ref_len);
        System.out.println("--------------------------------------");
    }
}
