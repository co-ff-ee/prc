
import java.util.*;

public class newfcfs {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        System.out.print("Enter number of processes: ");
        int n = sc.nextInt();

        int[] arrival = new int[n];
        int[] burst = new int[n];
        int[] completion = new int[n];
        int[] waiting = new int[n];
        int[] turnaround = new int[n];
        int[][] processData = new int[n][3]; // [arrival, processId, burst]

        for (int i = 0; i < n; i++) {
            System.out.println("Enter arrival time and burst time for Process " + (i + 1) + ":");
            arrival[i] = sc.nextInt();
            burst[i] = sc.nextInt();
            processData[i][0] = arrival[i];   // sort key 1
            processData[i][1] = i;            // process ID
            processData[i][2] = burst[i];     // burst time
        }

        // Sort by arrival time, then by process ID (to maintain input order)
        Arrays.sort(processData, (a, b) -> {
            if (a[0] == b[0]) return Integer.compare(a[1], b[1]);
            else return Integer.compare(a[0], b[0]);
        });

        int currentTime = 0;
        double totalWT = 0, totalTAT = 0;

        for (int i = 0; i < n; i++) {
            int pid = processData[i][1];
            arrival[pid] = processData[i][0];
            burst[pid] = processData[i][2];

            if (currentTime < arrival[pid]) {
                currentTime = arrival[pid]; // CPU idle
            }

            currentTime += burst[pid];
            completion[pid] = currentTime;
            turnaround[pid] = completion[pid] - arrival[pid];
            waiting[pid] = turnaround[pid] - burst[pid];

            totalWT += waiting[pid];
            totalTAT += turnaround[pid];
        }

        System.out.println("\nFCFS Scheduling:");
        System.out.printf("%-10s%-15s%-15s%-18s%-15s%-15s\n", "Process", "Arrival Time", "Burst Time", "Completion Time", "Waiting Time", "Turnaround Time");
        for (int i = 0; i < n; i++) {
            System.out.printf("P%-9d%-15d%-15d%-18d%-15d%-15d\n", i + 1, arrival[i], burst[i], completion[i], waiting[i], turnaround[i]);
        }

        System.out.printf("Average Waiting Time: %.2f\n", totalWT / n);
        System.out.printf("Average Turnaround Time: %.2f\n", totalTAT / n);
    }
}
