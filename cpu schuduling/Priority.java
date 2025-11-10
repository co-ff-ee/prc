import java.util.*; 
public class Priority { 
    public static void main(String[] args) { 
        Scanner sc = new Scanner(System.in); 
         System.out.print("Enter number of processes: "); 
        int n = sc.nextInt(); 
        int[] pid = new int[n]; 
        int[] arrival = new int[n]; 
        int[] burst = new int[n]; 
        int[] priority = new int[n]; 
        int[] completion = new int[n]; 
        int[] waiting = new int[n]; 
        int[] turnaround = new int[n]; 
        boolean[] done = new boolean[n]; 
        for (int i = 0; i < n; i++) { 
            System.out.println("Enter arrival time, burst time and priority for Process " + (i + 1) + ":"); 
            arrival[i] = sc.nextInt(); 
            burst[i] = sc.nextInt(); 
            priority[i] = sc.nextInt(); 
            pid[i] = i + 1; 
        } 
        int time = 0, completed = 0; 
        double totalWT = 0, totalTAT = 0; 
        while (completed < n) { 
            int idx = -1; 
            int bestPrio = Integer.MAX_VALUE; 
 
            for (int i = 0; i < n; i++) { 
                if (!done[i] && arrival[i] <= time) { 
                    if (priority[i] < bestPrio || (priority[i] == bestPrio && pid[i] < pid[idx])) { 
                        bestPrio = priority[i]; 
                        idx = i; 
                    } 
                } 
            } 
 
            if (idx == -1) { 
                time++; 
            } else { 
                completion[idx] = time + burst[idx]; 
                turnaround[idx] = completion[idx] - arrival[idx]; 
                waiting[idx] = turnaround[idx] - burst[idx]; 
                totalWT += waiting[idx]; 
                totalTAT += turnaround[idx]; 
                time = completion[idx]; 
                done[idx] = true; 
                completed++; 
            }                                                                                                                            
        } 
        System.out.println("\nPriority (Non-Preemptive) Scheduling:"); 
        System.out.printf("%-10s%-15s%-15s%-15s%-18s%-18s%-15s\n", 
                "Process", "Arrival", "Burst", "Priority", "Completion", "Turnaround", "Waiting"); 
                for (int i = 0; i < n; i++) { 
                 System.out.printf("P%-9d%-15d%-15d%-15d%-18d%-18d%-15d\n", 
                    pid[i], arrival[i], burst[i], priority[i], completion[i], turnaround[i], waiting[i]); 
        } 
         System.out.printf("Average Waiting Time: %.2f\n", totalWT / n); 
        System.out.printf("Average Turnaround Time: %.2f\n", totalTAT / n); 
    } 
}
