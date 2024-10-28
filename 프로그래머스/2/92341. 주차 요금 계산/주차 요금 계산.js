function solution(fees, records) {
    const [baseTime, baseFee, unitTime, unitFee] = fees;
    const parkingTime = {};
    const inTime = {};

    records.forEach(record => {
        const [time, car, type] = record.split(' ');
        const [hour, minute] = time.split(':').map(Number);
        const totalMinutes = hour * 60 + minute;

        if (type === 'IN') {
            inTime[car] = totalMinutes;
        } else {
            const parkedTime = totalMinutes - inTime[car];
            parkingTime[car] = (parkingTime[car] || 0) + parkedTime;
            delete inTime[car];
        }
    });

    for (const car in inTime) {
        const parkedTime = (23 * 60 + 59) - inTime[car];
        parkingTime[car] = (parkingTime[car] || 0) + parkedTime;
    }

    const result = Object.keys(parkingTime).sort().map(car => {
        const totalParkedTime = parkingTime[car];
        if (totalParkedTime <= baseTime) return baseFee;

        return (
            baseFee +
            Math.ceil((totalParkedTime - baseTime) / unitTime) * unitFee
        );
    });

    return result;
}
