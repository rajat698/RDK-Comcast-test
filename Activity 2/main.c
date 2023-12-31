#include <stdio.h>

/**
 * Splits the given integer array into two parts around the last element,
 * which is used as a pivot. Elements less than the pivot are moved to the
 * left of the pivot and elements greater than the pivot are moved to the
 * right of the pivot. This will be used for quick sort.
 *
 * @param arr The array to split
 * @param low The starting index to consider in the array
 * @param high The ending index to consider in the array
 * @return The final position of the pivot after partitioning the array
 */
int split(int arr[], int low, int high)
{
    // Setting last element as pivot
    int pivot = arr[high];

    int i = low - 1;
    for (int j = low; j <= high - 1; j++)
    {
        if (arr[j] < pivot)
        {
            i++;
            //Swap elements
            int temp = arr[i];
            arr[i] = arr[j];
            arr[j] = temp;
        }
    }

    //Swap elements
    int temp = arr[i + 1];
    arr[i + 1] = arr[high];
    arr[high] = temp;

    return i + 1;
}

/**
 * Sorts the given integer array using quicksort algorithm recursively.
 *
 * @param arr The array to sort
 * @param low The starting index to sort in the array
 * @param high The ending index to sort in the array
 */
void sort(int arr[], int low, int high)
{
    if (low < high)
    {
        int pivot = split(arr, low, high);
        // Recursive call to quicksort
        sort(arr, low, pivot - 1);
        sort(arr, pivot + 1, high);
    }
}

// Function to find the median of an array
//Note - This function does not have an empty array exception as it was not in the pseudo code provided.
float sortAndFindMedian(int numbers[], int length) {

    // Perform Quick Sort
    sort(numbers, 0, length - 1);

    /*
    Note - Length of the array is passed as a parameter and
    will be calculated in the driver function, because it is a good
    practice in C to pass the length as a parameter of function instead
    */

   //Check if the length of array is even or not
    if (length % 2 == 0) {

        //return average of middle two elements in case the length is even
        return (double)(numbers[length / 2 - 1] + numbers[length / 2]) / 2.0;

    } else {
        //return the middle element in case the length is off
        return (double)numbers[length / 2];
    }
}

// Function to print an array
void showArray(int arr[], int length) {
    for (int i = 0; i < length; i++) {
        printf("%d ", arr[i]);
    }
    printf("\n");
}

// Function to use our functions in various test cases
void testCase(int numbers[], int n) {
    
    printf("Given array: ");
    //Print unsorted array
    showArray(numbers, n);

    // Find the median
    float median = sortAndFindMedian(numbers, n);

    printf("Sorted array: ");
    //Print sorted array
    showArray(numbers, n);

    printf("Median: %.2f\n", median);
    printf("\n");
}

int main() {

    //Test case 1
    int numbers1[] = {6, 25, 2, 2, 11};
    int length1 = sizeof(numbers1) / sizeof(numbers1[0]);
    printf("Test Case 1\n");
    testCase(numbers1, length1);

    //Test case 2
    int numbers2[] = {101, -56, -81, -3, 50, 73};
    int length2 = sizeof(numbers2) / sizeof(numbers2[0]);
    printf("Test Case 2\n");
    testCase(numbers2, length2);

    //Test case 3
    int numbers3[] = {32, 17, 41, 11, 566, 92, 26, 62, 555, 31, 54};
    int length3 = sizeof(numbers3) / sizeof(numbers3[0]);
    printf("Test Case 3\n");
    testCase(numbers3, length3);

    //Test case 4
    int numbers4[] = {0, 0, 0, 0};
    int length4 = sizeof(numbers4) / sizeof(numbers4[0]);
    printf("Test Case 4\n");
    testCase(numbers4, length4);

    //Test case 5
    int numbers5[] = {1, -1, -1, 1};
    int length5 = sizeof(numbers5) / sizeof(numbers5[0]);
    printf("Test Case 5\n");
    testCase(numbers5, length5);

    return 0;
}
