GTI = int(input('What is your Income?: '))

if GTI > 0 and GTI <= 18200:
	print('Tax payable will be:',0,'Net Income will be:',GTI)
elif GTI > 18200 and GTI <= 37000:
	print('Tax payable will be:',(GTI-18200)*0.19,'Net Income will be:',GTI-((GTI-18200)*0.19))
elif GTI > 37000 and GTI <= 87000:
	print('Tax payable will be:',3572+((GTI-37000)*0.325),'Net Income will be:',GTI-(3572+((GTI-37000)*0.325)))
elif GTI > 87000 and GTI <= 180000:
	print('Tax payable will be:',19822+((GTI-87000)*0.37),'Net Income will be:',GTI-(19822+((GTI-87000)*0.37)))
else:
	print('Tax payable will be:',54532+((GTI-180000)*0.45),'Net Income will be:',GTI-(54532+((GTI-180000)*0.45)))


