# Online Food Ordering System (SWIGGY)

## Overview

As we all know now a days online food ordering is a trend. This python based project will allow us to register restaurants with there respective dishes and with ease customer can order food by typing dish name and our smart algorithm can give best dish according to price from registered restaurants.

## Specification

### Registered Restaurants

Swiggy can onboard new restaurants with there name and dishes. Restaurant owner can add, delete and update its registered dish

### Food Ordering Smart Algorithm

Swiggy can take order from user by typing dish name and our smart algorithm can give best dish with low price from restaurants

## Extra Features

#### 1. Customer can order from particular restaurant by typing its name
#### 2. Admin can watch all orders history and admin can also see order history by order number.

# User Guide

## For Restaurants
    "RE" -> restaurant registration 
    "AD" -> add dishes to particular restaurant
    "DD" -> delete dish of particular restaurant
    "UP" -> update price of particular restaurant
    "PT" -> update process time of particular restaurant
    "PM" -> print menu of particular restaurant

## For Users
    "OR" -> order from particular restaurant
    "OD" -> order dish directly

## For Admin
    "PO" -> print all orders
    "OO" -> print one order details
  
## Exit
    "EX" -> to Exit

## Commands Info :-
#### RE
    It takes input of how many restaurant you have to register
#### AD
    It takes two inputs "name of restaurant" to add dishes and "number of dishes" to be inserted
#### DD
    It takes two inputs "restaurant name" and "dish name" of particular restaurant
#### UP
    It takes three inputs "restaurant name", "dish name" and "updated Price"
#### PT
    It takes three inputs "restaurant name", "dish name" and "updated processing time"
#### PM
    it takes one input of "restaurant name"
#### OR
    It takes "restaurant name", "number of dishes" and "dishes names" as an inputs
#### OD
    It takes "number of dishes" as an input and also "dishes names" as an inputs
#### PO
    This command gives the details of all orders receive
#### OO
    It takes one input "order number" and It gives details about specific order