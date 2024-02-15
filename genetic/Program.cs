using Genetic;
using Microsoft.Extensions.DependencyInjection;
using Microsoft.Extensions.Hosting;
using Microsoft.Extensions.Logging;

var options = new Options(
    200,
    10,
    100,
    0.25f,
    0.01f,
    "To be or not to be, that is the question.",
    "abcdefghijklmnopqrstuvxz ,.T"
);

var host = new HostBuilder()
    .ConfigureLogging(logging => { logging.AddConsole(); })
    .ConfigureServices(services =>
    {
        services.AddScoped<Options>(_ => options).AddScoped<Random>().AddScoped<Stochastic>();
    })
    .UseOrleans(silo =>
    {
        silo.UseLocalhostClustering()
            .AddMemoryGrainStorageAsDefault()
            .AddMemoryGrainStorage("genetics");
    })
    .Build();

await host.StartAsync();

var client = host.Services.GetRequiredService<IClusterClient>();
await client.GetGrain<ITime>("Middle-earth").Elapse();

await host.StopAsync();