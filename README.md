# Spell Code!
I saw [this post](https://worldbuilding.stackexchange.com/questions/183368/magic-as-a-programming-language) about a magic based programming system, and after some thinking I realized that I could probably do some sort of JS/python interpreter that visualized a coded spell based on a JSON file's content. 

## Front-End/Visual
The visuals would likely be made through react or pygame, with some sort of on-click event to fire the spell.

## Structure
A spell would be set up like this in JSON:
```
{
    spell_name {
        "visual": {
            "color": string (hex code)
        },

        "properties": {
            "damage": {
                "damage_amount": int
                "damage_type": string
            }
        }
    }
}
```

This is all very tentative, but it will likely stay like this with some revisions.

## TO-DO
- Sprite Sheet Reader
- on_hit() function
- Reorganize code
- Search through filepath
