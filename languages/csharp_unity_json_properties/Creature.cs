using System;
using System.Collections.Generic;
using Newtonsoft.Json;
using Utils;

[System.Serializable]
public class Creature : Element
{
    [JsonProperty("appearance"), TextAttribute("")]
    public string appearance;
    [JsonProperty("weight"), Integer(0)]
    public int weight;
    [JsonProperty("height"), Integer(0)]
    public int height;
    [JsonProperty("species"), ReferenceAttribute(typeof(Species), true)]
    public string species;
    [JsonProperty("behaviour"), TextAttribute("")]
    public string behaviour;
    [JsonProperty("demeanour"), TextAttribute("")]
    public string demeanour;
    [JsonProperty("traits"), ReferenceAttribute(typeof(Trait), true)]
    public string traits;
    [JsonProperty("abilities"), ReferenceAttribute(typeof(Ability), true)]
    public string abilities;
    [JsonProperty("languages"), ReferenceAttribute(typeof(Language), true)]
    public string languages;
    [JsonProperty("birth_date"), Integer(0)]
    public int birthDate;
    [JsonProperty("location"), ReferenceAttribute(typeof(Location))]
    public string location;
    [JsonProperty("territory"), ReferenceAttribute(typeof(Territory))]
    public string territory;
    [JsonProperty("lore"), TextAttribute("")]
    public string lore;
    [JsonProperty("senses"), TextAttribute("")]
    public string senses;
    [JsonProperty("hit_points"), Integer(0)]
    public int hitPoints;
    [JsonProperty("armor_class"), Integer(0)]
    public int armorClass;
    [JsonProperty("challenge_rating"), Integer(0)]
    public int challengeRating;
    [JsonProperty("speed"), Integer(0)]
    public int speed;
    [JsonProperty("tt_str"), Integer(20)]
    public int ttStr;
    [JsonProperty("tt_int"), Integer(20)]
    public int ttInt;
    [JsonProperty("tt_con"), Integer(20)]
    public int ttCon;
    [JsonProperty("tt_dex"), Integer(20)]
    public int ttDex;
    [JsonProperty("tt_wis"), Integer(20)]
    public int ttWis;
    [JsonProperty("tt_cha"), Integer(20)]
    public int ttCha;
    [JsonProperty("actions"), ReferenceAttribute(typeof(Ability), true)]
    public string actions;
    [JsonProperty("reactions"), ReferenceAttribute(typeof(Construct), true)]
    public string reactions;
    [JsonProperty("alignment"), TextAttribute("")]
    public string alignment;
}
