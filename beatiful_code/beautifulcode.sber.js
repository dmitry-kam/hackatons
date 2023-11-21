/*
JS Converter array->hashmap
*/
function mapArrayToHashByKey(arrData, keyName) {
  try {
    let getType = variable =>
      Object.prototype.toString.call(variable).slice(8, -1).toLowerCase();
    let returnExcept = message => {
      throw new Error(message);
    };

    if (getType(keyName) !== 'string') {
      returnExcept('Argument `keyName` is incorrect');
    }

    const setKeyName = `_${keyName}s`;

    if (arrData === null || arrData === undefined) {
      return { [setKeyName]: [] };
    }
    if (getType(arrData) !== 'array') {
      returnExcept('Argument `arrData` is incorrect');
    }
    let result = arrData.reduce((acc, el) => {
      if (
        getType(el) === 'object' &&
        keyName in el &&
        ['string', 'number', 'boolean', 'undefined', 'null'].indexOf(
          getType(el[keyName])
        ) >= 0
      ) {
        acc[String(el[keyName])] = el;
      }
      return acc;
    }, {});

    result[setKeyName] = Object.keys(result);
    return result;
  } catch (e) {
    //console.error('mapArrayToHashByKey() error: ', e);
    return { _error: e };
  }
}