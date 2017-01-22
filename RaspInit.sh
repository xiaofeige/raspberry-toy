#!/bin/sh

passwd = "RenFei@123"

spawn sudo ssh -NfR 36000:127.0.0.1:22 ubuntu@www.luffyren.club -p 22

expect {
    "*password:" {send "$passwd\r"}}

