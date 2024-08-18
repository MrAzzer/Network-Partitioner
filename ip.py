#ip=str(input("input IPv4 address:"))
#mask=str(input("input network mask:"))
ip="10.10.12.13"
mask=29 #"255.255.255.224"
ip_tab=ip.split('.')
bin_mask_tab=[]
dec_mask2=[]
dec_mask=""

if isinstance(mask, str)==True:
    #print(isinstance(mask, str))
    mask_tab=mask.split('.')
else:
    pass

if mask in range(0, 33):
    for i in range(32):
        if i>=(mask):
            dec_mask+="0"
            #print("eo")
        if i<mask:
            dec_mask+="1"
        if i==7 or i==15 or i==23:
            dec_mask+='.'
        

        #print(dec_mask)
    bin_mask_tab=dec_mask.split(".")

    for i in range(4):
        dec_mask2.append(int(bin_mask_tab[i], 2))
    #print(dec_mask2, bin_mask_tab)
    mask_tab=dec_mask2


def Site_address(ip_tab, mask_tab, mask):
    bin_ip_tab=[]
    bin_ip_tab2=[]
    bin_mask_tab=[]
    bin_mask_tab2=[]
    site_address=""
    bin_site_address_tab=[]
    tab=[]
    mask_neg_tab=[]
    broadcast_tab=[]


    #print(mask, bin_mask_tab)

    for a in ip_tab: #tablica binarna IP
        bin_ip_tab.append(bin(int(a))[2::])
        var=str(bin(int(a))[2::])
        #print(len(var))
        if len(var)<=7:
            while len(var)<=7:
                var='0'+var
                #print(var)
        bin_ip_tab2.append(var)
        #print(bin_ip_tab2)

    for b in mask_tab: #tablica binarna maski
        bin_mask_tab.append(bin(int(b))[2::])
        var2=str(bin(int(b))[2::])
        #print(var2)
        if len(var2)<=7:
            while len(var2)<=7:
                var2="0"+var2
        bin_mask_tab2.append(var2)


    #print(bin_ip_tab2)
    #print(bin_mask_tab2)

    for i in range(4): #adres strony
        string1=str(bin_ip_tab2[i])
        string2=str(bin_mask_tab2[i])
        #print(string1)
        #print(string2)
        for j in range(8):
            #print(string1, string2)
            if string1[j]=="1" and string2[j]=="1":
                site_address+="1"
            else:
                site_address+="0"
        bin_site_address_tab.append(site_address)
        tab.append(int(site_address, 2))
        print(site_address)
        site_address=""
    #print(bin_site_address_tab, bin_mask_tab2)
    
    print("Site address:", tab)
    
    for i in range(4): #negacja maski
        mask_neg=""
        string3=str(bin_mask_tab2[i])
        for k in range(8):
            if string3[k]=="1":
                mask_neg+="0"
            else:
                mask_neg+="1"
        mask_neg_tab.append(mask_neg)
    #print(mask_neg_tab)

    for i in range(4): #adres rozgłoszeniowy
        string4=""
        for j in range(8):
            if int(bin_site_address_tab[i][j])==1 or int(mask_neg_tab[i][j])==1:
                string4+="1"
            else:
                string4+="0"
        broadcast_tab.append(int(string4, 2))


    print("Broadcast address:", broadcast_tab)

    print("IP range:[", tab[3], broadcast_tab[3], "]")
    print("Available hosts:", (broadcast_tab[2]-tab[2])*255+(broadcast_tab[3]-tab[3]-2))



if isinstance(mask, str)==True:
    print("IPv4:\n", ip_tab, "Mask:", mask_tab,)
else:
    print("IPv4:", ip_tab, "Mask:", mask_tab, "/", mask)


Site_address(ip_tab, mask_tab, mask)



net_part=int(input("How many hosts:"))
bimba=net_part
net_part=bin(net_part)
#print((net_part))
net_part=len((net_part))-2
mask=32-net_part
#print(mask)
if isinstance(mask, str)==True:
    #print(isinstance(mask, str))
    mask_tab=mask.split('.')
else:
    pass
dec_mask=""
dec_mask2=[]
bin_mask_tab=[]
mask_tab=[]
if mask in range(0, 33):
    for i in range(32):
        if i>=(mask):
            dec_mask+="0"
            #print("eo")
        if i<mask:
            dec_mask+="1"
        if i==7 or i==15 or i==23:
            dec_mask+='.'
        

        #print(dec_mask)
    bin_mask_tab=dec_mask.split(".")

    for i in range(4):
        dec_mask2.append(int(bin_mask_tab[i], 2))
    #print(dec_mask2, bin_mask_tab)
    mask_tab=dec_mask2

#print(mask_tab, mask)

print("#####################################################")
Site_address(ip_tab, mask_tab, mask=32-net_part)
print("Reserved hosts", bimba*2)

