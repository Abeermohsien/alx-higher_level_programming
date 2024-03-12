#!/usr/bin/node
exports.esrever = function (list) {
  let len = list.length - 1;
  let n = 0;
  while ((len - n) > 0) {
    const aux = list[len];
    list[len] = list[n];
    list[n] = aux;
    n++;
    len--;
  }
  return list;
};
