from typing import List
from collections import Counter,defaultdict
from math import *
from functools import reduce,lru_cache
import numpy as np
from heapq import *
from bisect import bisect_left

class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        n = len(words)
        words.sort(key = lambda x:(len(x),x))
        dp = [1]*n
        for j in range(1,n):
            for i in range(j):
                w1,w2 = words[i],words[j]
                if dp[i]>=dp[j] and self.predecessor(w1,w2):
                    dp[j] = dp[i]+1
        return max(dp)

    def predecessor(self,w1,w2):
        if len(w1)+1 !=len(w2):
            return False
        else:
            count_diff = 0
            for i in range(len(w1)):
                if w1[i]!=w2[i+count_diff]:
                    count_diff += 1
                    if count_diff>1:
                        return False
                    if w1[i]!=w2[i+count_diff]:
                        return False
            if count_diff == 0 or w1[-1]==w2[-1]:
                return True
            else :
                return False

sol = Solution()


# input
words = ["a","b","ba","bca","bda","bdca"]
# output
output = sol.longestStrChain(words)
# answer
answer = 4
print(output, answer, answer == output)

# input
words = ["xbc","pcxbcf","xb","cxbc","pcxbc"]
# output
output = sol.longestStrChain(words)
# answer
answer = 5
print(output, answer, answer == output)

# input
words = ["abcd","dbqca"]
# output
output = sol.longestStrChain(words)
# answer
answer = 1
print(output, answer, answer == output)

# input
words = ["qyssedya","pabouk","mjwdrbqwp","vylodpmwp","nfyqeowa","pu","paboukc","qssedya","lopmw","nfyqowa","vlodpmw","mwdrqwp","opmw","qsda","neo","qyssedhyac","pmw","lodpmw","mjwdrqwp","eo","nfqwa","pabuk","nfyqwa","qssdya","qsdya","qyssedhya","pabu","nqwa","pabqoukc","pbu","mw","vlodpmwp","x","xr"]
# output
output = sol.longestStrChain(words)
# answer
answer = 8
print(output, answer, answer == output)

# input
words = ["uiykgmcc","jrgbss","mhkqodcpy","lkj","bwqktun","s","nrctyzifwytjblwy","wrp","scqlcwmxw","irqvnxdcxoejuu","gmlckvofwyifmrw","wbzbyrcppaljigvo","lk","kfeouqyyrer","efzzpvi","ubkcitcmwxk","txihn","mdwdmbtx","vuzvcoaif","jwmboqvhpqodsj","wscfvrfl","pzye","waxyoxftvrgqmkg","wwdidopozinxxn","dclpg","xjsvlxktxs","ajj","pvsdastm","tatjxhygidhn","feafycxdxagn","irqvnxxoeuu","kwjo","tztoovsyfwz","prllrw","sclmx","bbmjnwaxcwaml","gl","wiax","uzvcoaif","ztovyfwz","qxy","zuexoxyp","qxyyrl","pvsdasvtm","femafycxdxaagn","rspvccjcm","wvyiax","vst","efzi","fjmdcc","icsinrbpql","ctybiizlcr","ntyzfwytjblw","tatjxhygidhpn","e","kykizdandafusu","pnepuwcsxl","kfeuqyyrer","afplzhbqguu","hvajtj","prll","ildzdimea","zueoxp","ezi","lqr","jkaagljikwamaqvf","mlzwhkxsn","rspvccbcjjtcm","wscfvrl","m","msygukwlkrqboc","pifojogoveub","bkcmwx","jercgybhss","wrpi","aicsinkgrbpqli","aplzbuu","sclcmxw","atpepgsz","govrcuuglaer","bdxjpsvlxkytxs","uikgm","bm","wvyhiqax","znvaasgfvqi","hatpepgsz","hrzebpa","bnfz","lybtqrfzw","taxhygihn","bjnfzk","mhqp","ide","znvcaasgfvqi","ftv","afplzhbqsguuu","thn","pdbccbe","mxevopfoimgjww","fjmdrcce","rspvccjjcm","jv","motnfwohwule","xjsvlxtxs","bqeb","eug","jftavwgl","rzebpa","lybtqrfazw","zuexoxp","jercgybhsys","hajtj","bkcitcmwxk","mbpvxsdastvtm","mowlznwhkxsn","dvenn","rsacxe","tatjxhygihn","cotybiizlcr","bbmnaxaml","pkwrpsi","nqpdbccbkxens","mbpbovxsdastvtm","mj","pxpsvikwekuq","qeug","dmelddga","aicsinkgrbpxqli","bdxjpsvlxktytxs","pkrllrxw","jkgljikwmaqf","iddie","ctybiizcr","nyzfwytjblw","yvuhmiuehspi","keuqre","wzbypaigvo","sck","uzcoaf","dlpg","ubkcpitlscmwxk","molzwhkxsn","pepuwcsxl","laplm","dclpgc","mahkxqodcpy","sclcmx","hvrzebpaz","bgovrcuuglaer","clazpulmw","yvuyhmiuehspiq","wzbycpaljigvo","sceqalciwmxw","hjytflmvsgv","u","hjyvxytfflhmvsgv","jkgjikwmaqf","fefycxdxagn","ftvw","ofncgxrkqvcr","spvcjc","pvsdastvtm","kykzdandaus","wbzbycppaljigvo","haytpepgsz","jmowlznwhkxsn","aplzhbguu","zvyz","nfvqi","jfvtavwsgl","xejnllhfulns","zhhvbiqiw","jkgljikwmaqvf","tyizc","irqvnxcxoejuu","clvazzpulmw","oncgxrqvcr","qlupvpdkhrm","mtnfwohwule","wwdidopzozinxxn","auiykgmcc","wscfvrfyl","pfksmrullrxw","jwmoqvhpqods","ftavwg","iddiea","kcmw","ykkwjwo","pe","aplzbguu","eu","bbmnaxal","ntyswtnlab","zhhhvbhbiqiw","jwmoqvpqods","kykzdndaus","bbmjnaxcwaml","zunvcaasgfvqi","icsingrbpql","sceqalciwmsxyw","yvuhmiuehsp","bxjsvlxktxs","waxoxftvrgqmkg","cogxxpaknks","scllvazzpulmw","tatjxhygeidhpn","ftvwg","tyz","nafvqi","oby","pgzpkhqog","irqvnxxoejuu","oxwpkxlakcp","bnf","oxwnpkxlakcp","bwqktu","ufybbaozoqk","ntydswtnlab","zvyfz","znaafvqi","npdbccbke","mhkqocpy","kuq","bjnfz","taxhyihn","kwrpsi","qifepmcatbdjlf","lzwhks","kfeuqre","mxevopfoimgww","spvcjcm","oncgxrkqvcr","jftavwsgl","soifcbya","jpzyeg","jwmboqvhpqods","lapulm","jrgbhss","xejfnllhfulns","zhhhvbbiqiw","km","kuqre","scxlzlvazzpulmw","ztvyfwz","wbzbycpaljigvo","rzbpa","vsastm","uybaooqk","dn","ykwjwo","ufybmvbaozoqk","nknm","mbpvsdastvtm","dpgzpxykhqog","wzbypajigvo","bnjnfzk","eollbigtftpdrd","zhbiqiw","yvuhiuehp","zhhhvbhbiqiwg","pfksrullrxw","pzyeg","aplzhbqguu","z","hvrzecbpazw","clvazpulmw","tajxhygihn","pgzpxykhqog","fefyxdxagn","wimomuvhn","lqrzw","xejnlhfulns","jhrc","xsxxs","slmx","jrgss","uikgmc","ncgqvcr","womuhn","aryouvtnmme","uzco","zhhhvbiqiw","hjytflhmvsgv","znvaasfvqi","kuqr","ojrpp","ztoovyfwz","zvz","pxpsviweuq","ufybaooqk","xy","jfvvtavwksvgl","raiachv","bmnaxl","rspvccjjtcm","pgzpxkhqog","xhbtfnqebaj","sceqalciwmsxw","jssctk","uzvcoaf","fefydxagn","jhrvc","mbj","raiahv","nrtyzifwytjblwy","mhqcp","jkgjkwmaqf","wscfvrfylhi","lqrz","ahabucermswyrvl","wxoxftvrgqmkg","ku","uyaoq","mhqocp","ykwjo","vstm","ofncgxrkqvcwr","dqvh","taxyihn","idie","bwqtu","tztoovyfwz","rspvcccjjtcm","uojrpp","wmomuhn","cotycbiizlxcr","nrtyzfwytjblw","ocbya","sceqlciwmxw","ajtj","rspvccbcjjthcm","kfeuqyyre","dmelddg","txyihn","ubkcitlscmwxk","ntyswtnla","bdxjpstvlxktytxs","odqdvbh","pxpsvikeewekuq","mdwdmbdtux","vs","bma","wzbypigvo","qxyy","vsstm","hbtnqeba","hrzebpaz","xhbtfnjsqebbaj","ahaucermswyrv","ddmbtx","zhhbiqiw","pxpsvikewekuq","odqdvgbh","bxjpsvlxktxs","jsck","fjmdc","mdwdmbdtx","jqxyyrl","pxpsvikweuq","ctybizcr","dqvbh","lpl","lqrfzw","ufybaozoqk","znvaafvqi","yvuhmiuehp","hvrzebpazw","pfksrllrxw","alzuu","xjsvxtxs","afplzhbqguuu","icsingrbpqli","hjxytflhmvsgv","femafycxdxagn","uyaoqk","gmlckvofwyifrw","cinrbpql","jrcgbhss","oxwpkxlkcp","jkagljikwamaqvf","eollbigtftpdrdy","rspvcjcm","socbya","clapulm","qeb","kwrpi","efzpi","hbtfnqebaj","kykizdnandafusu","sclvazzpulmw","efzzpvvi","jfvvtavwsvgl","mhqocpy","v","mbpbvxsdastvtm","irqvnxouu","hvaajtj","ofnlcgxrkqvcwr","hbtqeba","hbtqeb","jwmqpds","ntrnlhujdslco","zv","npdbccbken","mhp","ddb","prllw","mddmbtx","clazpulm","cogxxpaknkse","bkitcmwxk","oxwpklkcp","tyiz","jwmqvpqods","waxyoxftvrgqmkgb","afplzhbbqsgujuu","bwtu","jercgbhss","rsacx","mahkqodcpy","cotycbiizlcr","ahabucermswyrv","lupvpkhr","dvnn","b","atpepsz","ncgxqvcr","qe","ubkcitlcmwxk","lyqrfzw","wimomuhn","bbmnaxl","motnfwohrwule","yvuyhmiuehspi","jfvvtavwsgl","rac","fefdxagn","bwqkctun","uotjrpp","ddbtx","afplzhbbqsguuu","xss","xsxs","wvyiqax","kykizdandaus","npdbccbkens","r","oxwnpkxjlakcp","tzmteoovsyfwz","kykizdnandafuspu","ahabulcermswyrvl","xjsxxs","qxyyr","ck","xhbtfnqebbaj","nqpdbccbkens","mpvsdastvtm","zuexqoxyp","gmlkvofwyifrw","kmw","txhn","kykizdandausu","molznwhkxsn","lupvpdkhr","jwmqvpds","bktcmwx","wyiax","hzvaajtj","ddbx","pifojogveub","naafvqi","motnfwjohrwule","odqvbh","aicsingrbpqli","jopzyeg","lybtqrfazrw","pijogveub","xzejfnllhfulns","scxllvazzpulmw","irqyvnxdcxfoejuu","cogxpaknks","pdkwrpsi","wzbycpajigvo","xjsxtxs","irqvnxdcxfoejuu","xhbtfnjqebbaj","uybaoqk","oncgxqvcr","aj","pepuwsxl","lytqrfzw","nkm","jrgs","pkrllrw","wscfvrfyli","bbmjnaxcaml","jftavwg","vuzvcozaif","pifjogveub","cmogxxpaknkse","cinrbql","scqlciwmxw","ztvyfz","mxyevopfoimgjpww","soicbya","lupvpdkhrm","ahaucermsyrv","ufybmvbaouzoqk","bdxjpsvlxktxs","hjxytfflhmvsgv","hjvxytfflhmvsgv","nqpdbccbzkxens","wr","kykzdndus","iddimea","fjmdrcc","efzzpi","vsdastm","btqeb","pfkrllrxw","ocby","irqvnxxouu","ildzpdimea","lzwhkxsn","ilddimea","ufybvbaozoqk","mxyevopfoimgjww","jhr","kcmwx","dvn","uzcof","glw","hbtnqebaj","riahv","w","qeugv","kfeuqyre","ilrdzpdimea","lplm","icinrbpql","scqlcmxw","bbmjnaxaml","e","rsac","bf","jwmqvpqds","tzteoovsyfwz","rc","lzwhkxs","jkgljikwamaqvf","tybizc","aplzuu","nrtyzifwytjblw","pze","bktcmwxk","uiykgmc","jsctk","npdbccbe","tybizcr"]
# output
output = sol.longestStrChain(words)
# answer
answer = 15
print(output, answer, answer == output)
