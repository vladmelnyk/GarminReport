# GarminReport
Generate report for Garmin Connect running activity and analyze how does the increase in cadence impact my heart rate

Cadence in spm, Speed in min/km, Heart rate in bpm

The dataset is neither cleared nor has normal distribution. However, the results obtained from OLS regression showed that **rise in cadence by 1 spm results in the heart rate increase of 0.8885 bpm**. At some periods, even though the speed was constant during the training session - the increase in cadence would make heart rate spike a little. Now I have the proof that cadence is certainly having an impact on heart rate, with high t-stats and R-squared. 

![alt text](https://github.com/vladmelnyk/GarminReport/blob/master/OLS_result.png)

