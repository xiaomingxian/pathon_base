def main():
    s='1_c;2_v;3_f'
    print({i:i+1 for i in range(10)})
    print({v.split('_')[0]:v.split('_')[1] for v in s.split(';')})



if __name__ == '__main__':
    main()