class MaxHeap {
    constructor() {
        this.heap = [];
    }

    push(value) {
        this.heap.push(value);
        this._heapifyUp();
    }

    pop() {
        if (this.heap.length === 1) return this.heap.pop();
        const max = this.heap[0];
        this.heap[0] = this.heap.pop();
        this._heapifyDown();
        return max;
    }

    _heapifyUp() {
        let index = this.heap.length - 1;
        while (index > 0) {
            const parentIndex = Math.floor((index - 1) / 2);
            if (this.heap[index] <= this.heap[parentIndex]) break;
            [this.heap[index], this.heap[parentIndex]] = [this.heap[parentIndex], this.heap[index]];
            index = parentIndex;
        }
    }

    _heapifyDown() {
        let index = 0;
        const length = this.heap.length;

        while (true) {
            const leftChildIndex = 2 * index + 1;
            const rightChildIndex = 2 * index + 2;
            let largestIndex = index;

            if (
                leftChildIndex < length &&
                this.heap[leftChildIndex] > this.heap[largestIndex]
            ) {
                largestIndex = leftChildIndex;
            }

            if (
                rightChildIndex < length &&
                this.heap[rightChildIndex] > this.heap[largestIndex]
            ) {
                largestIndex = rightChildIndex;
            }

            if (largestIndex === index) break;

            [this.heap[index], this.heap[largestIndex]] = [this.heap[largestIndex], this.heap[index]];
            index = largestIndex;
        }
    }
}

function solution(n, k, enemy) {
    const maxHeap = new MaxHeap();
    let totalSoldiersUsed = 0;

    for (let i = 0; i < enemy.length; i++) {
        maxHeap.push(enemy[i]);
        totalSoldiersUsed += enemy[i];

        if (totalSoldiersUsed > n) {
            if (k > 0) {
                const maxEnemy = maxHeap.pop();
                totalSoldiersUsed -= maxEnemy;
                k--;
            } else {
                return i;
            }
        }
    }

    return enemy.length;
}
