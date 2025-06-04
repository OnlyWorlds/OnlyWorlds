using System;
using System.Collections.Generic;
using Newtonsoft.Json;
using Utils;

[System.Serializable]
public class World
{
    [JsonProperty("id"), TextAttribute("")]
    public string id;
    [JsonProperty("name"), TextAttribute("")]
    public string name;
    [JsonProperty("description"), TextAttribute("")]
    public string description;
    [JsonProperty("image_url"), TextAttribute("")]
    public string imageUrl;
    [JsonProperty("api_key"), TextAttribute("")]
    public string apiKey;
    [JsonProperty("version"), TextAttribute("")]
    public string version;
    [JsonProperty("user"), TextAttribute("")]
    public string user;
    [JsonProperty("time_format_equivalents"), TextAttribute("")]
    public string timeFormatEquivalents;
    [JsonProperty("time_format_names"), TextAttribute("")]
    public string timeFormatNames;
    [JsonProperty("time_basic_unit"), TextAttribute("")]
    public string timeBasicUnit;
    [JsonProperty("time_range_min"), Integer(0)]
    public int timeRangeMin;
    [JsonProperty("time_range_max"), Integer(0)]
    public int timeRangeMax;
    [JsonProperty("time_current"), Integer(0)]
    public int timeCurrent;
}
