#include <stdio.h>
#include <stdlib.h>

#define BUF_SIZE 8

const inline int max(int a, int b) {
    return a > b ? a : b;
}

int main(void) {

    char buf[BUF_SIZE];
    char* end;

    fgets(buf, BUF_SIZE, stdin);
	int n = strtol(buf, &end, 10);

	int* weight = malloc(n * sizeof(int));
	for (int i = 0; i < n; i++) {
        fgets(buf, BUF_SIZE, stdin);
	    weight[i] = strtol(buf, &end, 10);
    }

	int result = 0;
    int* lis = malloc(n * sizeof(int));
    int* lds = malloc(n * sizeof(int));

	for (int i = n - 1; i >= 0; --i) {
        lis[i] = 1;
        lds[i] = 1;
		for (int j = n - 1; j > i; --j) {
			if (weight[i] > weight[j]) lis[i] = max(lis[i], 1 + lis[j]);
			if (weight[i] < weight[j]) lds[i] = max(lds[i], 1 + lds[j]);
		}
		result = max(result, lis[i] + lds[i] - 1);
	}

	printf("%d\n", result);

    free(weight);
    free(lis);
    free(lds);

	return 0;
}
