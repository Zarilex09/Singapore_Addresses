import pandas as pd

sector_codes = {'01': 'Marina South',
                '02': 'Marina East',
                '03': 'Downtown Core',
                '04': 'Downtown Core',
                '05': 'Outram',
                '06': 'Outram',
                '07': 'Downtown Core',
                '08': 'Outram',
                '09': 'Bukit Merah',
                '10': 'Bukit Merah',
                '11': 'Queenstown',
                '12': 'Clementi',
                '13': 'Queenstown',
                '14': 'Queenstown',
                '15': 'Bukit Merah',
                '16': 'Bukit Merah',
                '17': 'Downtown Core',
                '18': 'Rochor',
                '19': 'Rochor',
                '20': 'Rochor',
                '21': 'Rochor',
                '22': 'Newton',
                '23': 'River Valley',
                '24': 'Tanglin',
                '25': 'Tanglin',
                '26': 'Bukit Timah',
                '27': 'Bukit Timah',
                '28': 'Bukit Timah',
                '29': 'Novena',
                '30': 'Novena',
                '31': 'Toa Payoh',
                '32': 'Kallang',
                '33': 'Kallang',
                '34': 'Geylang',
                '35': 'Toa Payoh',
                '36': 'Serangoon',
                '37': 'Geylang',
                '38': 'Geylang',
                '39': 'Kallang',
                '40': 'Geylang',
                '41': 'Bedok',
                '42': 'Marine Parade',
                '43': 'Marine Parade',
                '44': 'Marine Parade',
                '45': 'Bedok',
                '46': 'Bedok',
                '47': 'Bedok',
                '48': 'Tampines',
                '49': 'Changi Bay',
                '50': 'Changi',
                '51': 'Pasir Ris',
                '52': 'Tampines',
                '53': 'Hougang',
                '54': 'Sengkang',
                '55': 'Serangoon',
                '56': 'Ang Mo Kio',
                '57': 'Bishan',
                '58': 'Bukit Timah',
                '59': 'Clementi',
                '60': 'Jurong East',
                '61': 'Boon Lay',
                '62': 'Pioneer',
                '63': 'Tuas',
                '64': 'Jurong West',
                '65': 'Bukit Batok',
                '66': 'Bukit Batok',
                '67': 'Bukit Panjang',
                '68': 'Choa Chu Kang',
                '69': 'Western Water Catchment',
                '70': 'Western Water Catchment',
                '71': 'Lim Chu Kang',
                '72': 'Sungei Kadut',
                '73': 'Woodlands',
                '75': 'Sembawang',
                '76': 'Yishun',
                '77': 'Mandai',
                '78': 'Ang Mo Kio',
                '79': 'Seletar',
                '80': 'Ang Mo Kio',
                '81': 'Changi',
                '82': 'Punggol'
                }

district_codes = {'01': 1,
                  '02': 1,
                  '03': 1,
                  '04': 1,
                  '05': 1,
                  '06': 1,
                  '07': 2,
                  '08': 2,
                  '09': 4,
                  '10': 4,
                  '11': 5,
                  '12': 5,
                  '13': 5,
                  '14': 3,
                  '15': 3,
                  '16': 3,
                  '17': 6,
                  '18': 7,
                  '19': 7,
                  '20': 8,
                  '21': 8,
                  '22': 9,
                  '23': 9,
                  '24': 10,
                  '25': 10,
                  '26': 10,
                  '27': 10,
                  '28': 11,
                  '29': 11,
                  '30': 11,
                  '31': 12,
                  '32': 12,
                  '33': 12,
                  '34': 13,
                  '35': 13,
                  '36': 13,
                  '37': 13,
                  '38': 14,
                  '39': 14,
                  '40': 14,
                  '41': 14,
                  '42': 15,
                  '43': 15,
                  '44': 15,
                  '45': 15,
                  '46': 16,
                  '47': 16,
                  '48': 16,
                  '49': 17,
                  '50': 17,
                  '51': 18,
                  '52': 18,
                  '53': 19,
                  '54': 19,
                  '55': 19,
                  '56': 20,
                  '57': 20,
                  '59': 21,
                  '60': 22,
                  '61': 22,
                  '62': 22,
                  '63': 22,
                  '64': 22,
                  '65': 23,
                  '66': 23,
                  '67': 23,
                  '68': 23,
                  '69': 24,
                  '70': 24,
                  '71': 24,
                  '72': 25,
                  '73': 25,
                  '75': 27,
                  '76': 27,
                  '77': 26,
                  '78': 26,
                  '79': 28,
                  '80': 28,
                  '81': 17,
                  '82': 19
                  }

df = pd.read_excel('output_cleaned.xlsx', 'Cleaned', converters={'POSTAL':str})
# print(df['POSTAL'])

#res = df.dtypes
# print(res)

df['SECTOR'] = df['POSTAL'].str[:2]
# print(df['SECTOR'])

df["REGION"] = df['SECTOR'].apply(lambda x: sector_codes.get(x))
# print(df["REGION"])

df["DISTRICT"] = df['SECTOR'].apply(lambda x: district_codes.get(x))
# print(df["DISTRICT"])

writer = pd.ExcelWriter('output_cleaned.xlsx')
df.to_excel(writer, 'sect_dist')
writer.close()