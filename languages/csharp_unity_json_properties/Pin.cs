using System;
using System.Collections.Generic;
using Newtonsoft.Json;
using Utils;

[System.Serializable]
public class Pin : Element
{
    [JsonProperty("map"), ReferenceAttribute(typeof(Map))]
    public string map;
    [JsonProperty("element"), ReferenceAttribute(typeof(Element))]
    public string element;
    [JsonProperty("x"), Integer(0)]
    public int x;
    [JsonProperty("y"), Integer(0)]
    public int y;
    [JsonProperty("z"), Integer(0)]
    public int z;
}
