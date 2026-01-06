from collections import defaultdict
import heapq

class Twitter:

    def __init__(self):
        self.users = defaultdict(set)
        self.tweets = defaultdict(list)
        self.time = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.time += 1
        self.tweets[userId].append((self.time, tweetId))

    def getNewsFeed(self, userId: int) -> List[int]:
        ls = list({userId}.union(self.users[userId]))
        q = []
        heapq.heapify(q)
        count = 0
        ls1 = []

        for i in ls:
            if (i in self.tweets):
                heapq.heappush(q, (-1 * self.tweets[i][-1][0], self.tweets[i][-1][1], i, len(self.tweets[i]) - 1))
        
        while (len(q) != 0):
            time, tweet_id, user_id, index = heapq.heappop(q)
            ls1.append(tweet_id)
            count += 1

            if (count == 10):
                break
            
            if (index - 1 >= 0):
                heapq.heappush(q, (-1 * self.tweets[user_id][index - 1][0], self.tweets[user_id][index - 1][1], user_id, index - 1))
        
        return ls1
    
    def follow(self, followerId: int, followeeId: int) -> None:
        self.users[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.users[followerId].discard(followeeId)

# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)