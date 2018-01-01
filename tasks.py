from celery.task import task

suf = lambda n:"%d%s" % (n,{1: "st", 2:"nd", 3:"rd"}.get(n if n<20 else n%10, "th"))

@task
def fav_doctor():
    with open('doctor.txt','r+') as f:
        for line in f:
            nums = line.rstrip().split()

            print 'The {} doctor is my favorite'.format(suf(int(nums[0])))

            for num in nums[1:]:
                print 'Wait ! The {} doctor is my favorite'.format(suf(int(num)))

            last_sum = int(nums[-1])
            new_last_sum = last_sum + 1

            f.write(str(new_last_sum)+' ')
