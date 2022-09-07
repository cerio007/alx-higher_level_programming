#!/usr/bin/node
if (process.argv < 3) {
	console.log('No arguement');
}
else if (process.argv === 3) {
	console.log('Argument found');
}
else {
	console.log('Arguments found');
}
