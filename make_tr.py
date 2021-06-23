"""
How to use?
- Create an empty file named `orig.json` and paste the translation content to be MODIFIED (in the required format below).

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

- Change the `prefix` and `suffix` variables into anything you want.
- Run `python make_tr.py` to generate a file named `tr_test.json`
- Open `tr_test.json` to see the modified translation file.

"""

import json

filename = "orig.json"
new_filename = "tr_test.json"

prefix = ""
suffix = "_tr"

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
      new_item_obj["lowercase"] = prefix + _default_.lower() + suffix
      new_item_obj["uppercase"] = prefix + _default_.upper() + suffix
      new_item_obj["title"] = prefix + _default_.title() + suffix
      new_item_obj["capitalize"] = prefix + _default_.capitalize() + suffix
      new_item_obj["default"] = prefix + _default_ + suffix

      new_data[item] = new_item_obj

  fobj.close()

  """ Create new file """
  new_fobj = open(new_filename, "w")
  new_fobj.write(json.dumps(new_data, indent=2))
  new_fobj.close()
