using System;
using System.Collections.Generic;
using Newtonsoft.Json;
using Utils;

[System.Serializable]
public class Title : Element
{
    [JsonProperty("privileges"), TextAttribute("")]
    public string privileges;
    [JsonProperty("conditions"), TextAttribute("")]
    public string conditions;
    [JsonProperty("create_date"), Integer(0)]
    public int createDate;
    [JsonProperty("assign_date"), Integer(0)]
    public int assignDate;
    [JsonProperty("revoke_date"), Integer(0)]
    public int revokeDate;
    [JsonProperty("hierarchy"), Integer(0)]
    public int hierarchy;
    [JsonProperty("rights"), TextAttribute("")]
    public string rights;
    [JsonProperty("author"), ReferenceAttribute(typeof(Institution))]
    public string author;
    [JsonProperty("character"), ReferenceAttribute(typeof(Character))]
    public string character;
    [JsonProperty("location"), ReferenceAttribute(typeof(Location))]
    public string location;
    [JsonProperty("object"), ReferenceAttribute(typeof(Object))]
    public string tt_object;
    [JsonProperty("institution"), ReferenceAttribute(typeof(Institution))]
    public string institution;
    [JsonProperty("creature"), ReferenceAttribute(typeof(Creature))]
    public string creature;
    [JsonProperty("zone"), ReferenceAttribute(typeof(Zone))]
    public string zone;
    [JsonProperty("collective"), ReferenceAttribute(typeof(Collective))]
    public string collective;
    [JsonProperty("construct"), ReferenceAttribute(typeof(Construct))]
    public string construct;
}
