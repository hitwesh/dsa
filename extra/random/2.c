int a[] = {2, 4, 6, 8, 10};
int sum = 0;

for(int i = 0; i < 5; i++) {
    if(a[i] % 4 == 0)
        sum += a[i];
    else
        sum -= a[i];
}

printf("%d", sum);