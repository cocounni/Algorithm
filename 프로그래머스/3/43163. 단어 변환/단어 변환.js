function solution(begin, target, words) {
    if (!words.includes(target)) {
        return 0;
    }

    function isTranslatable(word1, word2) {
        let diffCount = 0;
        for (let i = 0; i < word1.length; i++) {
            if (word1[i] !== word2[i]) {
                diffCount++;
            }
            if (diffCount > 1) {
                return false;
            }
        }
        return diffCount === 1;
    }

    let queue = [[begin, 0]];
    let visited = new Set();
    visited.add(begin);

    while (queue.length > 0) {
        const [currentWord, transformations] = queue.shift();

        if (currentWord === target) {
            return transformations;
        }

        for (let nextWord of words) {
            if (!visited.has(nextWord) && isTranslatable(currentWord, nextWord)) {
                visited.add(nextWord);
                queue.push([nextWord, transformations + 1]);
            }
        }
    }
    return 0;
}
