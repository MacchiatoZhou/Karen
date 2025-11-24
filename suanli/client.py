import aiohttp
import asyncio


async def test_suanle_api(api_key: str, prompt: str = "Hello, how are you?"):
    """
    测试算了么API的简单函数
    """
    url = "https://api.suanli.cn/v1/chat/completions"
    headers = {
        'Authorization': f'Bearer {api_key}',
        'Content-Type': 'application/json'
    }

    data = {
        "model": "zai-org/GLM-4.5",
        "messages": [
            {"role": "user", "content": prompt}
        ]
    }

    async with aiohttp.ClientSession() as session:
        try:
            async with session.post(url, headers=headers, json=data) as response:
                result = await response.json()
                return result
        except Exception as e:
            return {"error": str(e)}


# 使用示例
async def main():
    api_key = "sk-y3lrg5LPWoVpWPzSKXtBToqYUQRs2p0Z9EAuWjrXwal41rCR"  # 替换成你的API Key

    # 简单测试
    response = await test_suanle_api(api_key, "你好，请简单介绍一下你自己，你是glm几")
    print(response)


# 运行测试
if __name__ == "__main__":
    asyncio.run(main())