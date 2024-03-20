# TLE Error Below --> need to convert to nlogn with binary search
# def jobScheduling(startTime, endTime, profit) -> int:
#         n = len(startTime)
#         dp = [0] * n
#         schedules = [(startTime[i], endTime[i], profit[i]) for i in range(n)]
#         schedules.sort(key = lambda x : x[0])
#         dp[0] = schedules[0][2]
#         for i in range(n):
#             prefix = 0
#             for j in range(i):
#                 if schedules[i][0] >= schedules[j][1]:
#                     prefix = max(prefix, dp[j])
#             dp[i] = prefix + schedules[i][2]
#         return max(dp)



def jobScheduling(startTime, endTime, profit) -> int:
        n = len(startTime)
        dp = [0] * n
        schedules = [(startTime[i], endTime[i], profit[i]) for i in range(n)]
        schedules.sort(key = lambda x : x[0])
        dp[0] = schedules[0][2]
        for i in range(n):
            prefix = 0
            for j in range(i):
                if schedules[i][0] >= schedules[j][1]:
                    prefix = max(prefix, dp[j])
            dp[i] = prefix + schedules[i][2]
        return max(dp)
    
    

print(jobScheduling([1,2,3,3], [3,4,5,6], [50,10,40,70]))
#print(jobScheduling([1,2,3,4,6], [3,5,10,6,9], [20,20,100,70,60]))