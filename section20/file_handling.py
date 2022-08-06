try:
    with open('test', 'w', encoding='utf-8') as fileObj:
        fileObj.write('Hi\n')
        fileObj.write('Another line, yay!\n')
        fileObj.write("Can't have enough of ñ\n")
        fileObj.write('También texto en español porque uso UTF-8\n')
        fileObj.write('¡Viva UTF-8!\n')
        fileObj.write('日本語も\n')
        fileObj.write('也简体中文\n')


except Exception as e:
    print(e)

finally:
    print('')

