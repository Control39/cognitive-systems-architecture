import json

with open(r'C:\Users\Z\Desktop\gordon\conversations.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

print(f"Всего диалогов: {len(data)}\n")

# Анализируем структуру
user_msgs = 0
assistant_msgs = 0
total_msgs = 0

for i, conv in enumerate(data[:3]):  # Смотрим первые 3
    if 'mapping' in conv:
        mapping = conv['mapping']
        print(f"Диалог {i}: {conv.get('title', 'No title')}")
        print(f"  Сообщений в mapping: {len(mapping)}")
        
        for key, node in list(mapping.items())[:3]:
            msg = node.get('message')
            if msg:
                role = msg.get('role')
                content = msg.get('content')
                if isinstance(content, list) and len(content) > 0:
                    text_content = content[0] if isinstance(content[0], str) else str(content[0])[:50]
                else:
                    text_content = str(content)[:50]
                
                print(f"    {role}: {text_content}...")
                total_msgs += 1
                if role == 'user':
                    user_msgs += 1
                elif role == 'assistant':
                    assistant_msgs += 1

print(f"\n📊 ИТОГО:")
print(f"Диалогов: {len(data)}")
print(f"Сообщений (в примере): {total_msgs}")
print(f"От тебя: {user_msgs}")
print(f"От DeepSeek: {assistant_msgs}")
