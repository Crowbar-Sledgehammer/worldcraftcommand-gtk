import winrm

s = winrm.Session('localhost:2223', auth=('sir', 'password'))
r = s.run_cmd('ipconfig', ['/all'])

print('r.status_code')
print(r.status_code)
print('r.std_out')
print(r.std_out)


# Combined with shared folder
