package PAGE_REPLACEMENT;
import java.io.*;

public class LRU {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int frames, hit = 0, fault = 0, ref_len;
        int[] buffer;
        int[] reference;
        int[][] mem_layout;
        int[] counter;

        System.out.print("Enter the Number of Frames: ");
        frames = Integer.parseInt(br.readLine());

        System.out.print("Enter the Length of Reference String: ");
        ref_len = Integer.parseInt(br.readLine());

        reference = new int[ref_len];
        mem_layout = new int[ref_len][frames];
        buffer = new int[frames];
        counter = new int[frames];

        
        for (int j = 0; j < frames; j++) {
            buffer[j] = -1;
            counter[j] = 0;
        }

        System.out.println("Please enter the reference string:");
        for (int i = 0; i < ref_len; i++) {
            reference[i] = Integer.parseInt(br.readLine());
            int search = -1;

            
            for (int j = 0; j < frames; j++) {
                if (buffer[j] == reference[i]) {
                    search = j;
                    hit++;
                    counter[j] = i + 1;
                    break;
                }
            }

            
            if (search == -1) {
                int min = 0;
                for (int j = 1; j < frames; j++) {
                    if (counter[j] < counter[min]) {
                        min = j;
                    }
                }
                buffer[min] = reference[i];
                counter[min] = i + 1;
                fault++;
            }

            
            for (int j = 0; j < frames; j++) {
                mem_layout[i][j] = buffer[j];
            }
        }

        
        System.out.print("\nReference String: ");
        for (int i = 0; i < ref_len; i++) {
            System.out.printf("%4d", reference[i]);
        }

        
        System.out.println("\n\nMemory Layout:");
        for (int i = 0; i < frames; i++) {
            System.out.printf("F%-2d |", i + 1);
            for (int j = 0; j < ref_len; j++) {
                if (mem_layout[j][i] == -1)
                    System.out.printf("%4s", "-1");  
                else
                    System.out.printf("%4d", mem_layout[j][i]);
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
