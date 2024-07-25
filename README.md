# Enunciado
Write a function that when two .csv formmated strings are given you return a new .CSV formatted string that contains the union betweem them, 
the first row of the new string should contain the header of the input strings.

first.csv
```
name,surname,address,age
John,Doe,120 jefferson st.,30
Jack,McGinnis,220 hobo Av.,43
John,Repici,120 Jefferson St.,24
Stephen,Tyler,7452 Terrace road,60
,Blankman,,30
Joan,Jet,at Terrace plc,40
```

second.csv
```
name,surname,address,age
Aloysius, Alfalfa, Corrientes 800,20
Alfred, Jones, Alem 234,20
Gramma, Gerty , Carranza 1234, 34
Electric, Android,,
```

expected.csv
```
name,surname,address,age
John,Doe,120 jefferson st.,30
Jack,McGinnis,220 hobo Av.,43
John,Repici,120 Jefferson St.,24
Stephen,Tyler,7452 Terrace road,60
,Blankman,,30
Joan,Jet,at Terrace plc,40
Aloysius, Alfalfa, Corrientes 800,20
Alfred, Jones, Alem 234,20
Gramma, Gerty , Carranza 1234, 34
Electric, Android,,
```
