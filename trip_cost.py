#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 10 17:20:31 2016

@author: NABRARPOUR4
"""

def hotel_cost(nights):
    return 140 * nights

def plane_ride_cost(city):
    if city == 'Charlotte':
        return 183
    elif city == 'Tampa':
        return 220
    elif city == 'Pittsburgh':
        return 222
    elif city == 'Los Angeles':
        return 475 

def rental_car_cost(days):
    if days >= 7:
        return days * 40 - 50
    elif days >= 3:
        return days * 40 - 20
    else: 
        return days * 40
        
def trip_cost(city, days):
    nights = days
    return sum([plane_ride_cost(city), hotel_cost(nights), 
                rental_car_cost(days)])

trip_cost('Tampa', 15)
2870
trip_cost('Los Angeles', 15)
3125

def trip_cost(city, days, spending_money):
    nights = days
    return sum([plane_ride_cost(city), hotel_cost(nights), 
                rental_car_cost(days), spending_money]) 
print trip_cost('Los Angeles', 5, 600) 
1955