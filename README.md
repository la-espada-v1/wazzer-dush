# wazzer-dush
hardware/embedded system to regulate the tempeture of SHOWERSSS (a cubicle or bath in which a person stands under a spray of water to wash.)


# basic idea of the dush thingy

two water buckets, one filled with hot, the other with cold water. theyre
linked with tubes to two separate pumps, who are connected to their 
controller - BB-L298. the BB-L298 is connected to Raspberry Pi5, to which is 
connected the sns-tmp-ds18b20 tempeture sensor that checks the tempeture 
in the shower head (where the tubes of the pumps with hot water and cold
water are mixed) and later gives signal to the RPi5