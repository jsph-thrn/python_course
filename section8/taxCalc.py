# Locale zh_CN.UTF-8
# 2022年 06月 27日 星期一 17:20:09 CDT
# José Luis Yáñez Páez

# Tax Calculator

def taxCalc(price, tax):
    return price * (1 + (tax) / 100)

rawPrice = float(input('Enter the price free of taxes: '))
taxRate = float(input('Enter the tax rate (%): '))
netPrice = taxCalc(rawPrice, taxRate)
print(f'Net payment: {netPrice}')

