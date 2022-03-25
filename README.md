### 依赖配置：
1. 安装python3.10
2. 安装python依赖(可能需要管理员运行) `pip -r dependencies.txt`
3. 安装deno `iwr https://deno.land/install.ps1 -useb | iex`
4. 在浏览器端安装tampermonkey 并将mediaControllerHook.js导入其中
5. 进入程序目录
6. 运行`deno run --allow-net glue.ts`
7. 运行`python scanner.py`
