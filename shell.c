#include <stdio.h>

void print(int arr[], int cnt)
{
    int i;
    for (i = 0; i < cnt; i++)
    {
        printf(" %d ", arr[i]);
    }
    printf("\n");
}

void shell_sort(int arr[], int cnt)
{
    int gap = 0;
    while (gap <= cnt)
    {
        gap = gap * 3 + 1;
    }
    printf("%d\n", gap);
    int i, k, temp;
    while (gap > 0)
    {
        printf("------------\n");
        for (i = gap; i < cnt; i++)
        {
            printf("============\n");
            temp = arr[i];
            k = i - gap;
            while ((k >= 0) && (arr[k] > temp))
            {
                arr[k + gap] = arr[k];
                k = k - gap;
            }
            arr[k + gap] = temp;
        }
        gap = (gap - 1) / 3;
    }
}

int main(void)
{
    int arr[] = {5, 4, 3, 2, 1};
    const int cnt = 5;
    print(arr, cnt);
    shell_sort(arr, cnt);
    print(arr, cnt);
}
