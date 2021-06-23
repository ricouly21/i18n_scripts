"""
How to use?
- Create an empty file named `orig.json` and paste the translation content to be FIXED (in the required format below).

Required format of `orig.json`:
{
   "famgenix": {
     "default": "FamGenix"
   },
   "en": {
     "default": "Englisch"
   },
   {...}
}

- Run `python fixer.py` to generate a file named `new.json`
- Open `new.json` to see the modified translation file.

"""

import json

filename = "orig.json"
new_filename = "new.json"

if __name__ == "__main__":
  """ Read original file """
  fobj = open(filename, 'r')
  data = json.loads(fobj.read())

  new_data = {}

  for item in data:
    item_obj = data[item]

    _default_ = "{}".format(item_obj["default"])

    if _default_ == "":
      continue
    else:
      new_item_obj = item_obj
      new_item_obj["lowercase"] = _default_.lower()
      new_item_obj["uppercase"] = _default_.upper()
      new_item_obj["title"] = _default_.title()
      new_item_obj["capitalize"] = _default_.capitalize()

      new_data[item] = new_item_obj

  fobj.close()

  """ Create new file """
  new_fobj = open(new_filename, "w")
  new_fobj.write(json.dumps(new_data, indent=2))
  new_fobj.close()
