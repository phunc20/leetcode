## Not yet
```bash
[phunc20@homography-x220t 193-phone_numbers]$ grep "[0-9]\{3\}\() \|-\)[0-9]\{3\}-[0-9]\{4\}" file.txt
987-123-4567
(123) 456-7890
[phunc20@homography-x220t 193-phone_numbers]$
```


## Final answer
**`grep "\(^[0-9]\{3\}-\|^([0-9]\{3\}) \)[0-9]\{3\}-[0-9]\{4\}$" file.txt`**

This exercise is, as being labeled, quite easy, except that one might have to **pay attention to** which characters
should and should not be **escaped** in `grep`.

```bash
[phunc20@homography-x220t 193-phone_numbers]$ grep "\(^[0-9]\{3\}-\|^([0-9]\{3\}) \)[0-9]\{3\}-[0-9]\{4\}$" file.txt
987-123-4567
(123) 456-7890
[phunc20@homography-x220t 193-phone_numbers]$
```
