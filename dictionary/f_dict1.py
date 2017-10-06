signals = {'green': 'go', 'yellow': "go faster",'red':'smile for the camera'}
print(list(signals.keys())) # print keys
print(list(signals.values()))    #rint values
print(list(signals.items())) # print pair

save_signals = signals  # refer & depnded dict from signals
copy_signals = signals.copy()   # copy original signals
signals['blue'] = 'confuse everyone'
print(save_signals)
print(copy_signals)