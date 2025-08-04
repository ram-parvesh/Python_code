class Solution:
    def findmediansortedarray(self, nums1,nums2):
        A,B = nums1,nums2
        total =len(nums1) + len(nums2)
        half = total//2

        if len(B) < len(A):
            A,B = B,A
        l,r =0, len(A)-1
        
        while true:
            i = (l+r)//2  ##A
            j = half - i-2 ##B
            Aleft = A[i] if i>=0 else float("-infinity")
            Aright = A[i+1] if (i+1) < len(A) else float("infinity")
            Bleft = B[j] if j>=0 else float("-infinity")
            Bright = B[j+1] if (j+1) <len(B) else float("infinity")

        #partition
        if Aleft <=Bright and Bleft <=Aright:
            ##add
            if total %2:
                return min(Aright , Bright)
            return (max(Aleft, Blaft) +min(Arightm, Bright))/2
        elif Aleft>Bright:
            r = i-1
        else:
            l = i+1