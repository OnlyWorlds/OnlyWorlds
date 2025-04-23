using System;
using System.Collections.Generic;
using Newtonsoft.Json;
using Utils;

[System.Serializable]
public class Element
{
    [JsonProperty("Id"), TextAttribute("")]
    public string id;
    [JsonProperty("Name"), TextAttribute("")]
    public string name;
    [JsonProperty("Description"), TextAttribute("")]
    public string description;
    [JsonProperty("Supertype"), TextAttribute("")]
    public string supertype;
    [JsonProperty("Subtype"), TextAttribute("")]
    public string subtype;
    [JsonProperty("Image_URL"), TextAttribute("")]
    public string imageUrl;
    [JsonProperty("World")]
    public string worldId;
}
