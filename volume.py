import csv
print('Monthly')
mons = {'01':'Jan', '02':'Feb', '03':'Mar', '04': 'Apr', '05': 'May', "06": 'Jun', "07": 'Jul', '08': 'Aug', '09': 'Sep', '10': 'Oct', '11': 'Nov', '12':'Dec'}
nsw = {'Jan': 0, "Feb": 0, "Mar": 0,"Apr": 0,"May":0,"Jun":0,"Jul":0,"Aug":0,"Sep":0,"Oct":0,"Nov":0, "Dec":0}
qld = {'Jan': 0, "Feb": 0, "Mar": 0,"Apr": 0,"May":0,"Jun":0,"Jul":0,"Aug":0,"Sep":0,"Oct":0,"Nov":0, "Dec":0}
sa = {'Jan': 0, "Feb": 0, "Mar": 0,"Apr": 0,"May":0,"Jun":0,"Jul":0,"Aug":0,"Sep":0,"Oct":0,"Nov":0, "Dec":0}
vic = {'Jan': 0, "Feb": 0, "Mar": 0,"Apr": 0,"May":0,"Jun":0,"Jul":0,"Aug":0,"Sep":0,"Oct":0,"Nov":0, "Dec":0}
tas = {'Jan': 0, "Feb": 0, "Mar": 0,"Apr": 0,"May":0,"Jun":0,"Jul":0,"Aug":0,"Sep":0,"Oct":0,"Nov":0, "Dec":0}
nsw_tot = {'Jan': 0, "Feb": 0, "Mar": 0,"Apr": 0,"May":0,"Jun":0,"Jul":0,"Aug":0,"Sep":0,"Oct":0,"Nov":0, "Dec":0}
qld_tot = {'Jan': 0, "Feb": 0, "Mar": 0,"Apr": 0,"May":0,"Jun":0,"Jul":0,"Aug":0,"Sep":0,"Oct":0,"Nov":0, "Dec":0}
sa_tot = {'Jan': 0, "Feb": 0, "Mar": 0,"Apr": 0,"May":0,"Jun":0,"Jul":0,"Aug":0,"Sep":0,"Oct":0,"Nov":0, "Dec":0}
vic_tot = {'Jan': 0, "Feb": 0, "Mar": 0,"Apr": 0,"May":0,"Jun":0,"Jul":0,"Aug":0,"Sep":0,"Oct":0,"Nov":0, "Dec":0}
tas_tot = {'Jan': 0, "Feb": 0, "Mar": 0,"Apr": 0,"May":0,"Jun":0,"Jul":0,"Aug":0,"Sep":0,"Oct":0,"Nov":0, "Dec":0}
nsw_sum = 0
qld_sum = 0
sa_sum = 0
vic_sum = 0
tas_sum = 0
counter = 0
with open(r'C:\Users\km0152\OneDrive - Agriculture\Documents\Electricity_data.csv', newline='') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    
    next(reader)
    for row in reader:
        x = row[0].split('/')
        if row[0] != '':
            counter += 1
            nsw_sum += float(row[1])
            qld_sum += float(row[2])
            sa_sum += float(row[3])
            vic_sum += float(row[4])
            tas_sum += float(row[5])
          
            nsw[mons.get(x[1])] += float(row[1])*float(row[6])/12
            qld[mons.get(x[1])] += float(row[2])*float(row[7])/12
            sa[mons.get(x[1])] += float(row[3])*float(row[8])/12
            vic[mons.get(x[1])] += float(row[4])*float(row[9])/12
            tas[mons.get(x[1])] += float(row[5])*float(row[10])/12
            nsw_tot[mons.get(x[1])] += float(row[6])/12
            qld_tot[mons.get(x[1])] += float(row[7])/12
            sa_tot[mons.get(x[1])] += float(row[8])/12
            vic_tot[mons.get(x[1])] += float(row[9])/12
            tas_tot[mons.get(x[1])] += float(row[10])/12
            
        else:
            break
    '''writer = csv.writer(csvfile, delimiter = ',')
    writer.writerow(6)'''

for i in mons:
    print(mons[i])
    print("NSW: ${}".format(round(nsw[mons[i]]/nsw_tot[mons[i]],2)))
    print("QLD: ${}".format(round(qld[mons[i]]/qld_tot[mons[i]],2)))
    print("SA: ${}".format(round(sa[mons[i]]/sa_tot[mons[i]],2)))
    print("VIC: ${}".format(round(vic[mons[i]]/vic_tot[mons[i]],2)))
    print("TAS: ${}".format(round(tas[mons[i]]/tas_tot[mons[i]],2)))
    print("NEM: ${}".format(round((nsw[mons[i]]+qld[mons[i]]+sa[mons[i]]+vic[mons[i]]+tas[mons[i]])/(nsw_tot[mons[i]]+qld_tot[mons[i]]+sa_tot[mons[i]]+vic_tot[mons[i]]+tas_tot[mons[i]]),2)))
print("\nQuarters")
quarters = {'March':['Jan', 'Feb', 'Mar'], 'June':['Apr','May','Jun'], 'September':['Jul','Aug','Sep'],'December':['Oct','Nov','Dec']}

for a,b in quarters.items():
    print(a)
    nsw_cp = 0
    nsw_ct = 0
    qld_cp = 0
    qld_ct = 0
    sa_cp = 0
    sa_ct = 0
    vic_cp = 0
    vic_ct = 0
    tas_cp = 0
    tas_ct = 0
    for e in b:
        
        nsw_cp += nsw[e]
        nsw_ct += nsw_tot[e]
        qld_cp += qld[e]
        qld_ct += qld_tot[e]
        sa_cp += sa[e]
        sa_ct += sa_tot[e]
        vic_cp += vic[e]
        vic_ct += vic_tot[e]
        tas_cp += tas[e]
        tas_ct += tas_tot[e]
    print("NSW: ${}".format(round(nsw_cp/nsw_ct,2)))
    print("QLD: ${}".format(round(qld_cp/qld_ct,2)))
    print("SA: ${}".format(round(sa_cp/sa_ct,2)))
    print("VIC: ${}".format(round(vic_cp/vic_ct,2)))
    print("TAS: ${}".format(round(tas_cp/tas_ct,2)))
    print("NEM: ${}".format(round((nsw_cp+qld_cp+sa_cp+vic_cp+tas_cp)/(nsw_ct+qld_ct+sa_ct+vic_ct+tas_ct),2)))

            
print("\nYearly")
print("NSW: ${}".format(round(sum(nsw.values())/sum(nsw_tot.values()),2)))
print("QLD: ${}".format(round(sum(qld.values())/sum(qld_tot.values()),2)))
print("SA: ${}".format(round(sum(sa.values())/sum(sa_tot.values()),2)))
print("VIC: ${}".format(round(sum(vic.values())/sum(vic_tot.values()),2)))
print("TAS: ${}".format(round(sum(tas.values())/sum(tas_tot.values()),2)))
print("NEM: ${}".format(round((sum(nsw.values())+sum(qld.values())+sum(sa.values())+sum(vic.values())+sum(tas.values()))/(sum(nsw_tot.values())+sum(qld_tot.values())+sum(sa_tot.values())+sum(vic_tot.values())+sum(tas_tot.values())),2)))

print("\nAverage")
print("NSW: ${}".format(round(nsw_sum/counter,2)))
print("QLD: ${}".format(round(qld_sum/counter,2)))
print("SA: ${}".format(round(sa_sum/counter,2)))
print("VIC: ${}".format(round(vic_sum/counter,2)))
print("TAS: ${}".format(round(tas_sum/counter,2)))
print("NEM: ${}".format(round((nsw_sum+qld_sum+sa_sum+vic_sum+tas_sum)/(counter*5),2)))
