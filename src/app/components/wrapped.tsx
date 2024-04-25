import React from "react";

interface JsonData {
  emoji_counts: Record<string, number>;
  name_counts: Record<string, number>;
  top_emojis_per_name: {
    [name: string]: Record<string, number>;
  };
}

const EmojiStatistics: React.FC<{ data: JsonData }> = ({ data }) => {
  return (
    <div className="flex items-center justify-center">
      {Object.entries(data.emoji_counts).map(([emoji, count]) => (
        <p key={emoji}>
          {emoji}: {count}
        </p>
      ))}
      {Object.entries(data.name_counts).map(([name, count]) => (
        <p key={name}>
          {name}: {count}
        </p>
      ))}
      {Object.entries(data.top_emojis_per_name).map(([name, emojis]) => (
        <div key={name}>
          <h3>{name}</h3>
          {Object.entries(emojis).map(([emoji, count]) => (
            <p key={emoji}>
              {emoji}: {count}
            </p>
          ))}
        </div>
      ))}
    </div>
  );
};

export default EmojiStatistics;
