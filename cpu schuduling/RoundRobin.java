import java.util.*;

public class RoundRobin {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        System.out.print("Enter number of processes: ");
        int n = sc.nextInt();

        int[] pid = new int[n];
        int[] arrival = new int[n];
        int[] burst = new int[n];
        int[] remaining = new int[n];
        int[] completion = new int[n];
        int[] waiting = new int[n];
        int[] turnaround = new int[n];
        boolean[] done = new boolean[n]; 
        boolean[] inQueue = new boolean[n]; 

        for (int i = 0; i < n; i++) {
            System.out.println("Enter arrival and burst time for Process " + (i + 1) + ":");
            arrival[i] = sc.nextInt();
            burst[i] = sc.nextInt();
            remaining[i] = burst[i]; 
            pid[i] = i + 1; 
        }

        System.out.print("Enter time quantum: ");
        Float quantum = sc.nextFloat();

        sc.close();

        Queue<Integer> queue = new LinkedList<>(); 
        int time = 0;
        int completed = 0; 

        
        for (int i = 0; i < n; i++) {
            if (arrival[i] <= time && !inQueue[i]) {
                queue.add(i);
                inQueue[i] = true;
            }
        }

        while (completed < n) { 
            if (queue.isEmpty()) {
               
                time++;
                for (int i = 0; i < n; i++) {
                    if (arrival[i] <= time && !inQueue[i] && !done[i]) { 
                        queue.add(i);
                        inQueue[i] = true;
                    }
                }
                continue; 
            }

            int idx = queue.poll(); 

            
            Float execTime = Math.min(quantum, remaining[idx]);
            
            time += execTime; 
            remaining[idx] -= execTime; 

            
            
            
            for (int i = 0; i < n; i++) {
               
                if (arrival[i] > (time - execTime) && arrival[i] <= time && !inQueue[i] && !done[i]) {
                    queue.add(i);
                    inQueue[i] = true;
                }
            }

            if (remaining[idx] == 0) { 
                completion[idx] = time; 
                turnaround[idx] = completion[idx] - arrival[idx]; 
                waiting[idx] = turnaround[idx] - burst[idx]; 
                done[idx] = true; 
                completed++; 
                inQueue[idx] = false; 
            } else {
                
                queue.add(idx);
                
            }
        }

        
        double totalWT = 0; 
        double totalTAT = 0; 
        for (int i = 0; i < n; i++) {
            totalWT += waiting[i]; 
            totalTAT += turnaround[i]; 
        }

        double avgWT = totalWT / n;
        double avgTAT = totalTAT / n; 


        System.out.println("\nRound Robin Scheduling (Preemptive):");
        System.out.printf("%-10s%-15s%-15s%-18s%-18s%-15s\n",
                "Process", "Arrival", "Burst", "Completion", "Turnaround", "Waiting");

        for (int i = 0; i < n; i++) {
            System.out.printf("P%-9d%-15d%-15d%-18d%-18d%-15d\n",
                    pid[i], arrival[i], burst[i], completion[i], turnaround[i], waiting[i]);
        }

        System.out.printf("Average Waiting Time: %.2f\n", avgWT);
        System.out.printf("Average Turnaround Time: %.2f\n", avgTAT); 
    }
}