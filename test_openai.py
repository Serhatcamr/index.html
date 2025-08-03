# Test OpenAI import
import openai
print("✅ OpenAI library imported successfully!")

# Test basic functionality
try:
    print("🔍 Testing OpenAI client creation...")
    client = openai.OpenAI(api_key="test-key")
    print("✅ OpenAI client created successfully!")
except Exception as e:
    print(f"❌ Error creating client: {e}")

print("🎉 Import test completed!") 