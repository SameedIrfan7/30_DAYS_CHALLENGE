#include <stdio.h>

void split(int[], int, int);
void combine(int[], int, int, int);

int main() {
    int a[20], i, n;

    printf("Enter the no. of elements:\t");
    scanf("%d", &n);

    printf("Enter the elements:\n");
    for (i = 0; i < n; i++) {
        scanf("%d", &a[i]);
    }

    split(a, 0, n - 1);

    printf("The sorted array is:\n");
    for (i = 0; i < n; i++) {
        printf("%d\t", a[i]);
    }

    return 0;
}

void split(int a[], int low, int high) {
    int mid;
    if (low < high) {
        mid = (low + high) / 2;
        split(a, low, mid);
        split(a, mid + 1, high);
        combine(a, low, mid, high);
    }
}

void combine(int a[], int low, int mid, int high) {
    int c[20], i = low, j = mid + 1, k = low;

    while (i <= mid && j <= high) {
        c[k++] = (a[i] < a[j]) ? a[i++] : a[j++];
    }

    while (i <= mid) {
        c[k++] = a[i++];
    }

    while (j <= high) {
        c[k++] = a[j++];
    }

    for (i = low; i <= high; i++) {
        a[i] = c[i];
    }
}
