function solution(name, yearning, photo) {
    let obj = {};
    
    // name과 yearning을 key와 value로 묶어줌
    for(let i = 0; i < name.length; i++){
        obj[name[i]] = yearning[i];
    }
    
    return photo.map(value => 
    value.map(v => obj[v] ? obj[v] : 0)
         .reduce((acc, cur) => acc + cur, 0)
    );
    
    return answer;
}