level = int(input("What's your crafting level?"))

from statistics import mean

ds = {
    20 : [ 9999 ] ,      21 : [ 9999 ] , 22 : [ 9999 ] ,     23 : [ 9999 ] , 24 : [ 9999 ] ,
    25 : [ 9999 ] ,      26 : [ 9999 ] , 27 : [ 9999 ] ,     28 : [ 9999 ] , 29 : [ 9999 ] , 
    30 : [ 9999 ] ,      31 : [ 9999 ] , 32 : [ 9999 ] ,     33 : [ 9999 ] , 34 : [ 9999 ] ,
    35 : [ 9999 ] ,      36 : [ 9999 ] , 37 : [ 9999 ] ,     38 : [ 9999 ] , 39 : [ 9999 ] ,
    40 : [ 9999 ] ,      41 : [ 9999 ] , 42 : [ 9999 ] ,     43 : [ 9999 ] , 44 : [ 9999 ] ,
    45 : [ 9999 ] ,      46 : [ 9999 ] , 47 : [ 9999 ] ,     48 : [ 9999 ] , 49 : [ 9999 ] ,
    50 : [ 9999 ] ,      51 : [ 9999 ] , 52 : [ 9999 ] ,     53 : [ 9999 ] , 54 : [ 9999 ] ,
    55 : [  371 ] ,      56 : [  379 ] , 57 : [  364 ] ,     58 : [ 9999 ] , 59 : [  275 ] ,
    60 : [ 9999 ] ,      61 : [ 9999 ] , 62 : [ 345 , 354 ], 61 : [ 9999 ] , 61 : [ 9999 ] ,
    65 : [ 9999 ] ,      66 : [ 9999 ] , 67 : [ 9999 ] ,     68 : [ 9999 ] , 69 : [ 9999 ] ,
    70 : [ 9999 ] ,      71 : [ 9999 ] , 72 : [ 9999 ] ,     73 : [ 9999 ] , 74 : [ 9999 ] ,
    75 : [ 9999 ] ,      76 : [ 9999 ] , 77 : [ 9999 ] ,     78 : [ 9999 ] , 79 : [ 9999 ] ,
    80 : [ 9999 ] ,      81 : [ 9999 ] , 82 : [ 9999 ] ,     83 : [ 9999 ] , 84 : [ 9999 ] ,
    85 : [ 258 , 246 ] , 86 : [ 9999 ] , 87 : [ 9999 ] ,     88 : [ 9999 ] , 89 : [ 9999 ] ,
    90 : [ 9999 ] ,      91 : [ 9999 ] , 92 : [ 9999 ] ,     93 : [ 9999 ] , 94 : [ 9999 ] ,
    95 : [ 258 , 246 ] , 96 : [ 9999 ] , 97 : [ 9999 ] ,     98 : [ 9999 ] , 99 : [  227 ]
}
for level in ds:
    restock = 5400/((mean(ds[level])/100)*540+105)
    print("level" , level , ":" , round(restock,2) , "m /hr.")




1 set = 6.5 minutes
5 sets = 450 sanctity
100 resources = 50 sanctity

stock up between 0-17 resources
restock resources every 6 trips
39.25 minutes to make a full round (restocked 0-100 resources)
