using System;
using System.Collections.Generic;
using Newtonsoft.Json;
using Utils;

[System.Serializable]
public class Map : Element
{
    [JsonProperty("background_color"), TextAttribute("")]
    public string backgroundColor;
    [JsonProperty("hierarchy"), Integer(0)]
    public int hierarchy;
    [JsonProperty("width"), Integer(0)]
    public int width;
    [JsonProperty("height"), Integer(0)]
    public int height;
    [JsonProperty("depth"), Integer(0)]
    public int depth;
    [JsonProperty("parent_map"), ReferenceAttribute(typeof(Map))]
    public string parentMap;
    [JsonProperty("location"), ReferenceAttribute(typeof(Location))]
    public string location;
}
